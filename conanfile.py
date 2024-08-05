from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class HelloConan(ConanFile):
    name = 'myobject'
    version = '1.0'
    exports_sources = "CMakeLists.txt", "myobject*"
    generators = "CMakeDeps", "CMakeToolchain"
    settings = "os", "compiler", "arch", "build_type"
    
    def package(self):
        cmake = CMake(self)
        cmake.install()

    def layout(self):
        cmake_layout(self)
    
    def package_info(self):
        self.cpp_info.objects = ['lib/myobject.o']

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    