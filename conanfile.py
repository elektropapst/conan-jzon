from conans import ConanFile, CMake


class Jzon(ConanFile):
    name = "Jzon"
    version = "2.1"
    settings = "os", "compiler", "build_type", "arch"
    url = "http://zguy.github.io/Jzon/"
    license = "MIT"
    description = "Jzon is a JSON parser for C++ with focus on a nice and easy to use interface. No dependencies, " \
                  "except the standard library. "

    def source(self):
        self.run("git clone https://github.com/elektropapst/Jzon.git")

    def build(self):
        cmake = CMake(self.settings)
        self.run("cmake %s/Jzon %s" % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build .")

    def package(self):
        self.copy("*.h", dst="include", src="Jzon")
        self.copy("*.lib", dst="lib", src=".")
        self.copy("*.a", dst="lib", src=".")
        self.copy("*.so", dst="lib", src=".")

    def package_info(self):
        self.cpp_info.libs = ["Jzon"]
