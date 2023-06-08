import setuptools

setuptools.setup(
    name = "mlflow-cmd",
    version = "0.1",
    description = "MLflow command tool",
    author = "Seungha Son",
    author_email = "linuxias@gmail.com",
    license="MIT",
    url = "https://github.com/linuxias/mlflow-command-tool",
    packages = setuptools.find_packages(),
    keywords = ["mlflow", "cmd"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
    ]
)