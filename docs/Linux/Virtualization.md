# Virtualization

[Comparison of platform virtual machines](https://en.wikipedia.org/wiki/Comparison_of_platform_virtual_machines)

[Linux KVM](https://www.linux-kvm.org/)

[Xen](https://en.wikipedia.org/wiki/Xen)

[VMware ESX](https://en.wikipedia.org/wiki/VMware_ESX)

[vSphere](https://en.wikipedia.org/wiki/VSphere)

## KVM vs Hyper-V vs Container Runtimes

### KVM (Kernel-based Virtual Machine)

- Linux-native virtualization module.
- Turns the Linux kernel into a Type 1 bare-metal hypervisor.

### Hyper-V

- Microsoft's hardware virtualization product.
- Provides Type 1 hypervisor capabilities on Windows.
- Used extensively in WSL2 to provide native Linux kernels on Windows.

### Modern Container Runtime Engines (containerd, CRI-O)

- Not hypervisors. They use Linux cgroups and namespaces to isolate processes.
- They do not emulate hardware but rather share the host OS kernel.
- Much lighter and faster startup compared to full VMs.

## Example

```text
Review this cheatsheet and adapt the commands to your environment before execution.
```
