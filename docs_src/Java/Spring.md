# Spring


All Spring beans are managed - they "live" inside a container, called "application context".

Second, each application has an entry point to that context. Web applications have a Servlet, JSFuses a el-resolver, etc. Also, there is a place where the application context is bootstrapped and all beans - autowired. In web applications this can be a startup listener.

Autowiring happens by placing an instance of one bean into the desired field in an instance of another bean. Both classes should be beans, i.e. they should be defined to live in the application context.

What is "living" in the application context? This means that the context instantiates the objects, not you. I.e. - you never make new UserServiceImpl() - the container finds each injection point and sets an instance there.


## Spring and AWS

[A New Way of Using Email for Support Apps: An AWS Tutorial](
https://www.toptal.com/aws/new-way-email-support-app-aws?utm_campaign=blog_post_new_way_email_support_app_aws&utm_medium=email&utm_source=blog_subscribers )
