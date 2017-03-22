---
title: WPF
category: dotNET
tags: .NET C#
comments: true
---

## Useful Links

[WPF tutorial](http://wpftutorial.net/)

[WPF Documentation](http://msdn.microsoft.com/en-us/library/vstudio/ms754130.aspx)

[WPF Samples](https://github.com/Microsoft/WPF-Samples)

[WPF Tools](http://www.codeproject.com/Articles/22126/Mole-For-Visual-Studio-Visualizer-For-All-Project)

### Application

```xml
<Application x:Class="ExpenseIt.App"
     xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
     StartupUri="MainWindow.xaml">
    <Application.Resources>
    </Application.Resources>
</Application>
```

### Commands

[WPF Commands](http://msdn.microsoft.com/en-us/library/ms752308(v=vs.110).aspx)

WPF provides a set of predefined commands. The command library consists of the following classes: ApplicationCommands, NavigationCommands, MediaCommands, EditingCommands, and the ComponentCommands.

```xml
<StackPanel>

<StackPanel.ContextMenu>
    <ContextMenu>
      <MenuItem Command="ApplicationCommands.Properties" />
    </ContextMenu>
</StackPanel.ContextMenu>
  <Menu>
    <MenuItem Command="ApplicationCommands.Paste" />
  </Menu>
  <TextBox /></StackPanel>

<Window.InputBindings>
  <KeyBinding Key="B"
              Modifiers="Control" 
              Command="ApplicationCommands.Open" /></Window.InputBindings>
```

### Page

```xml
<Page
  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
  x:Class="ExampleNamespace.ExampleCode"
  >
  <StackPanel>
    <Button>Button 1</Button>
    <Button>Button 2</Button>
    <Button>Button 3</Button>
  </StackPanel>
</Page>
```

### Styles

```xml
<Window.Resources><!--A Style that affects all TextBlocks-->
<Style TargetType="TextBlock">
  <Setter Property="HorizontalAlignment" Value="Center" />
  <Setter Property="FontFamily" Value="Comic Sans MS"/>
  <Setter Property="FontSize" Value="14"/></Style></Window.Resources>
<!--A Style that extends the previous TextBlock Style--><!--This is a "named style" with an x:Key of TitleText-->
<Style BasedOn="{StaticResource {x:Type TextBlock}}"
       TargetType="TextBlock"
       x:Key="TitleText">
  <Setter Property="FontSize" Value="26"/>
  <Setter Property="Foreground">
  <Setter.Value>
      <LinearGradientBrush StartPoint="0.5,0" EndPoint="0.5,1">
        <LinearGradientBrush.GradientStops>
          <GradientStop Offset="0.0" Color="#90DDDD" />
          <GradientStop Offset="1.0" Color="#5BFFFF" />
        </LinearGradientBrush.GradientStops>
      </LinearGradientBrush>
    </Setter.Value>
  </Setter></Style>
```
  
### Triggers

```xml
<Style x:Key="SpecialButton" TargetType="{x:Type Button}">
  <Style.Triggers>
    <Trigger Property="Button.IsMouseOver" Value="true">
      <Setter Property = "Background" Value="Red"/>
    </Trigger>
    <Trigger Property="Button.IsPressed" Value="true">
      <Setter Property = "Foreground" Value="Green"/>
    </Trigger>
  </Style.Triggers></Style>
```

