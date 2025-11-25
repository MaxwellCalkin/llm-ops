from setuptools import setup, find_packages

setup(
    name="llm-ops",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "llm-ops=llm_ops.main:main",
        ],
    },
    python_requires=">=3.6",
    author="User",
    description="CLI to install global AI agent workflows for Windsurf and Augment.",
)
