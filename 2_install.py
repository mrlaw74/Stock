import subprocess
import os

# 1. Extract TA-Lib source code
subprocess.run(["tar", "-xzf", "ta-lib-0.4.0-src.tar.gz"])

# 2. Navigate to the extracted directory
os.chdir("ta-lib/")

# 3. Configure, make, and install TA-Lib
configure_command = ["sudo", "./configure", "--prefix=/usr/local/share"]
# sudo ./configure --prefix=/usr/local/share
subprocess.run(["sudo", "make"])
subprocess.run(["sudo", "make", "install"])

# 4. Install Python wrapper using pip
subprocess.run(["pip", "install", "ta-lib"])

# 5 Install pip install vnstock
subprocess.run(["pip", "install", "vnstock"])
# pip install vnstock