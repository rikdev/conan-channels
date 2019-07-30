from conans import ConanFile, CMake, tools


class ChannelsConan(ConanFile):
    name = "Channels"
    version = "0.2.1"
    license = "MIT"
    url = "https://github.com/rikdev/channels"
    description = "Another C++ signal/slot library"
    topics = ("conan", "signal/slot")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "COW/0.1.0@rikdev/stable"
    build_requires = "cmake_installer/3.15.1@conan/stable"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/rikdev/channels.git", "master")
        tools.replace_in_file("CMakeLists.txt", "if(FETCH_DEPENDENCIES)",
                              "include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)\n"
                              "conan_basic_setup()\n"
                              "if(FETCH_DEPENDENCIES)")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["FETCH_DEPENDENCIES"] = "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["ENABLE_TOOLING"] = "OFF"
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*channels.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Channels"]
        if not self.settings.os == "Windows":
            self.cpp_info.cxxflags = ["-pthread"]
