from distutils.core import setup

setup(
    name = "siricoin",
    packages = ["siricoin"],
    version = "0.1",
    license= "MIT",
    description = "SiriCoin RPC Client",
    author = "Bastel Pichi",
    author_email = "pichi@pichisdns.com",
    url = "https://github.com/BastelPichi/siricoin-py",
    download_url = "https://github.com/BastelPichi/siricoin-py/archive/01.tar.gz",
    keywords = ["SiriCoin", "Crypto", "RPC"],
    install_requires = [
        "web3",
        "eth-account",
        "requests"
    ],
)
