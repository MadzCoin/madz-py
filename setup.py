from distutils.core import setup
from pathlib import Path

readme = Path(__file__).parent
readme = (readme / "README.md").read_text()

setup(
    name = "sirious",
    packages = ["sirious"],
    version = "0.5",
    license= "MIT",
    description = "Sirious RPC Client",
    long_description = readme,
    long_description_content_type = "text/markdown",
    author = "Bastel Pichi",
    author_email = "pichi@pichisdns.com",
    url = "https://github.com/Sirious-io/sirious-py",
    download_url = "https://github.com/BastelPichi/siricoin-py/archive/refs/tags/0.5.tar.gz",
    keywords = ["Sirious", "Crypto", "RPC"],
    install_requires = [
        "web3",
        "eth-account",
        "requests"
    ],
)
