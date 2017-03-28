#Python installation

### You can choose to follow the following steps [Link to Python installation](https://developers.google.com/earth-engine/python_install)
### Or you can find these steps below




The Earth Engine Python API is distributed as a Python package that is hosted on Github. The following instructions give an overview of installing the Google Earth Engine Python API. To use the Earth Engine Python API you'll need to install the client library and its dependencies on your computer and then set up authentication credentials.

Installing the client library

Ubuntu Linux & Mac OS X installation

After the initial set up, the installation flows for Mac OS X and Ubuntu are nearly identical.

1. Set up pip and Python

PIP is a package manager for Python. The following installation instructions assume that you are using it.

Ubuntu Linux

Verify that you have Python 2.6 or 2.7:

python --version
      
If needed, install 2.6 or 2.7 with apt-get. Then pip can be installed with:

sudo apt-get install python-pip
      
Mac OS X

The installation instructions assume that you are using Mac OS X 10.9+, the Homebrew Mac OS package manager, and the pip Python package manager. Feel free to use a different package manager such as Fink or MacPorts if you prefer.

Homebrew can be installed with:

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      
Then pip (and Python) can be installed with the following command:

brew install python
      
Note: Mac OS X ships with a default version of Python 2. Homebrew should install its own Python 2.7, which we'll be using to avoid interfering with the system-level configuration.

Regardless of you choice of package manager, verify that you have Python 2.6 or 2.7:

python --version
      
2. Install Google APIs Client Library

The Google APIs Client Library for Python provides support for authenticating to the Earth Engine servers. The library can be installed from the Python Package index by running the following command:

sudo pip install google-api-python-client
          
Alternatively, the library can be built from the source code, available on GitHub.

3. Ensure that a crypto library is available

If no error is returned by the following command, you can skip this step.

python -c "from oauth2client import crypt"
      
If there's an error, you'll need to install a Cryto library on your system. You can install either PyCrypto (recommended) or both OpenSSL and pyOpenSSL.

pyCrypto

The pyCrypto library can be installed from the Python Package Index by running the following command:

sudo pip install pyCrypto
        
OpenSSL

OpenSSL is a toolkit that implements Secure Sockets Layer protocol. To check if the OpenSSL library is installed on your system, run the following command, which will print the version of the library:

openssl version
        
On Ubuntu/Debian, the library can be installed with:

sudo apt-get install openssl
        
On Mac, the library can be installed with:

brew install openssl
        
pyOpenSSL

pyOpenSSL is a Python wrapper for the OpenSSL library. The pyOpenSSL library can be installed from the Python Package Index by running the following command:

sudo pip install 'pyOpenSSL>=0.11'
        
Alternatively, the library can be built from the source code, available on GitHub.

4. Install the Earth Engine Python API

The Earth Engine Python library can be installed from the Python Package Index by running the following command:

sudo pip install earthengine-api
        
Installing manually from source code

To install the Earth Engine API manually, download the package from the PyPI download page and expand the archive file:

tar -zxvf earthengine-api-VERSION.tar.gz
        
Next switch into the expanded directory and run the setup script:

cd earthengine-api-VERSION
python setup.py install
        
Windows Installation

Installing PIP and virtualenv in Windows.

Installing earthengine-api on Windows7 with 64bit Python2.7.

Uninstalling the Library

To uninstall using the PIP package manager, run the following command.

pip uninstall google-api-python-client
      
Uninstalling manually

The setup script installs numerous Python files. To uninstall, simply find the files and remove them from your system.

On a Linux system, the package may be found here:

/usr/local/lib/python2.7/dist-packages/earthengine_api-0.#.###.egg-info
/usr/local/lib/python2.7/dist-packages/ee/
        
On a Windows system with the default Python installation path, the package may be found here:

C:\Python27\Lib\site-packages\earthengine_api-0.#.###-py2.7.egg
        
Note that the file locations may vary depending on you system configuration.

Setting Up Authentication Credentials

The Earth Engine APIs use the OAuth 2.0 protocol for authenticating clients. In order to authenticate, you will need to first setup a credentials file on your computer that authorizes access to Earth Engine on behalf of your Google account. You can trigger the process of creating the credentials file by calling the ee.Initialize() method from the following terminal command:

python -c "import ee; ee.Initialize()"
      
If you call ee.Initialize() without any arguments (as the preceding command does), the API tries to read credentials from a file located in a subfolder of your home directory. The location of the credentials file depends on your operating system. On Linux or OSX, the location is

$HOME/.config/earthengine/credentials
      
On Windows, the location is

%UserProfile%\.config\earthengine\credentials
      
If a credentials file is not found, you will be presented with an error message that includes instructions for creating a new credentials file. The basic steps are:

Open up a new terminal window, and copy the command that was presented in the error message into the new terminal window. This command runs a Python script (authenticate.py) that starts the process for creating a credentials file.
The script (authenticate.py) attempts to open a web page (https://accounts.google.com/o/oauth2/auth). If you are not already signed in with your Google Account, you will be prompted to do so at this time. Once authenticated, the web page will ask you to authorize access to Earth Engine data.
Click accept, and the web page will present you with an authorization code.
Copy the authorization code, and paste in the terminal where the Python script (authenticate.py) is running. The script will write credentials file to the correct location on your file system.
Testing the installation

To test that authentication has been correctly setup, run the following script.

```python
# Import the Earth Engine Python Package
import ee

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

# Print the information for an image asset.
image = ee.Image('srtm90_v4')
print(image.getInfo())
```
      
If everything is installed correctly, the metadata for an image should be printed.

Coding in the Python API

The Earth Engine Python API is identical to the Javascript API with a few exceptions. For example, you need to import the Earth Engine library to your Python scripts with

`import ee`
      
In addition to syntactic differences between JavaScript and Python (e.g. declare a user function in Python with 'def' instead of 'function'), logical methods are capitalized in Python to avoid reserved words: And(), Or(), Not() instead of and(), or() not(). Map output is currently not supported.
