# Use the built-in `platform` module to print out the following info:
import platform
#placeholder = "remove me :)"
plat = platform.platform() 
compiler = platform.python_compiler()
py_vers = platform.python_version()
system = platform.system()
release = platform.release()
sys_processor =  platform.processor()

print(f"{'Platform:':>10} {plat}",)  # platform.platform()
print(f"{'Compiler:':>10} {compiler}",)  # platform.python_compiler()
print(f"{'Python:':>10} {py_vers}",)  # platform.python_version()
print(f"{'System:':>10} {system}",)  # platform.system()
print(f"{'Release:':>10} {release}",)  # platform.release()
print(f"{'System:':>10} {sys_processor}",)  # platform.processor()