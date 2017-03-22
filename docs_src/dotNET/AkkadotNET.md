---
title: Akka.NET Examples
category: dotNET
tags: .NET C# Akka
---
# Akka.NET Examples


// To install Akka.NET Distributed Actor Framework, run the following command in the Package Manager Console

// PM> Install-Package Akka

// PM> Install-Package Akka.Remote

// Installing with Topshelf is as easy as calling <myApp>.exe install on the command line.

```C#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Add these two lines
using Akka;
using Akka.Actor;
using Topshelf;   // http://topshelf.readthedocs.io/en/latest/configuration/quickstart.html

internal class Program
{
	private static void Main(string[] args)
	{
		// ‘x’ exposes all of the host level configuration
		HostFactory.Run(x =>
        {
            x.Service<ActorService>(s =>     //  telling Topshelf that there is a service of type ActorService. service configuration options exposed through the ‘s’ parameter.
            {
                s.ConstructUsing(name => new ActorService()); // build an instance of the service; new or pull from IoC container
                s.WhenStarted(service => service.Start());
                s.WhenStopped(service => service.Stop());
                ////continue and restart directives are also available
				//s.WhenPaused(service => service.Pause());
				//s.WhenContinued(service => service.Continue());
				//s.WhenShutdown(service => service.Shutdown());
				
            });

            x.RunAsLocalSystem(); // service ‘run as’ the ‘local system’. Alternatively x.RunAsLocalSystem(); x.RunAs("username", "password");  x.RunAsPrompt();
            x.UseAssemblyInfoForServiceInfo();
			
			//x.SetDescription("Orchestrator Host"); 
			//x.SetDisplayName("Orchestrator"); // display name for the winservice in the windows service monitor
            //x.SetServiceName("Orchestrator"); // service name for the winservice in the windows service monitor
			//x.SetInstanceName("MyService"); // instance name of the service, which is combined with the base service name and separated by a $.
        });
    }
}

// <summary>
/// This class acts as an interface between the application and TopShelf
/// </summary>
public class ActorService
{
    private ActorSystem system;

    public void Start()
    {
        // Create a new actor system (a container for actors)
        this.system = ActorSystem.Create("MainSystem");
    }

    public async void Stop()
    {
        //this is where you stop your actor system
        await this.system.Terminate();
    }
	
	private void Create()
	{
		// Create your actor and get a reference to it.
		// This will be an "ActorRef", which is not a
		// reference to the actual actor instance
		// but rather a client or proxy to it.
		var job = system.ActorOf<JobActor>("Job");
		//or: var myActor = system.ActorOf(Props.Create<JobActor>());
		
		// Send a message to the actor
		job.Tell(new Message<string>("Hello World"));
	}
}

// Example immutable message class - C# 7.0
public class Message<T>
{
	public Message(T data)
	{
		this.Data = data;
	}
	
	public T Data { get; }
	
	// Allow convesion to a tuple 
	public void Deconstruct(out T data) { data = this.Data; }
}

// Example of ReceiveActor
public class JobActor: ReceiveActor
{
  private readonly ILoggingAdapter log = Context.GetLogger();
  
  public JobActor()
  {
    Receive<Message<string>>(message => {
      log.Info("Received String message: {0}", message.Data);
	  // Console.WriteLine(message.Data);
	  
	  // reply back
      Sender.Tell(message);
    });
  }
}



// Example of untyped actor

public class MyActor : UntypedActor
{
    private ActorRef logger = Context.ActorOf<LogActor>();

    // if any child, e.g. the logger above. throws an exception
    // apply the rules below
    // e.g. Restart the child, if 10 exceptions occur in 30 seconds or
    // less, then stop the actor
    protected override SupervisorStrategy SupervisorStrategy()
    {
        return new OneForOneStrategy( //or AllForOneStrategy
            maxNumberOfRetries: 10,
            duration: TimeSpan.FromSeconds(30),
            decider: Decider.From(x =>
            {
                //Maybe we consider ArithmeticException to not be application critical
                //so we just ignore the error and keep going.
                if (x is ArithmeticException) return Directive.Resume;
                //Error that we cannot recover from, stop the failing actor
                else if (x is NotSupportedException) return Directive.Stop;
                //In all other cases, just restart the failing actor
                else return Directive.Restart;
             }));
    }
}

// Example of long-running operation in an Actor - PipeTo / Become / Stash

/*
If you stick a long-running operation inside your Receive method then your actors will be unable to process any messages, including system messages, until that operation finishes. And if it’s possible that the operation will never finish, it’s possible to deadlock your actor.
The solution to this is simple: you need to encapsulate any long-running I/O-bound or CPU-bound operations inside a Task and make it possible to cancel that task from within the actor.
Here’s an example of how you can use behavior switching, stashing, and control messages to do this.

https://petabridge.com/blog/akka-actors-finite-state-machines-switchable-behavior/

*/
public class FooActor : ReceiveActor, IWithUnboundedStash
{

	private Task _runningTask;
	private CancellationTokenSource _cancel;

	public IStash Stash {get; set;}

	public FooActor(){
		_cancel = new CancellationTokenSource();
		Ready();
	}

	private void Ready(){
		Receive<Start>(s => {
			var self = Self; // closure
			_runningTask = Task.Run(() => {
				// ... work
			}, _cancel.Token).ContinueWith(x =>
			{
				if(x.IsCancelled || x.IsFaulted)
					return new Failed();
				return new Finished();
			}, TaskContinuationOptions.ExecuteSynchronously)
			.PipeTo(self);

			// switch behavior
			Become(Working);
		})
	}

	private void Working(){
		Receive<Cancel>(cancel => {
			_cancel.Cancel(); // cancel work
			BecomeReady();
		});
		Receive<Failed>(f => BecomeReady());
		Receive<Finished>(f => BecomeReady());
		ReceiveAny(o => Stash.Stash());
	}

	private void BecomeReady(){
		_cancel = new CancellationTokenSource();
		Stash.UnstashAll();
		Become(Ready);
	}
}
```
