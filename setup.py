from cx_Freeze import setup, Executable

setup(
    name = "macgyver",
    version = "0.1",
    description = "Help MacGyver !",
    options = {"build_exe": {"include_files": ['img', 'level.txt']}},
    executables = [Executable("run.py")],
)
