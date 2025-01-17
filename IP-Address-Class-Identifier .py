
 ##@AUTHOR Rahul Majhi##

 ##Here’s a draft of a legal copyright license for your tool, **"IP-Address-Class-Identifier"**:



### Copyright License for "IP-Address-Class-Identifier"

#**Copyright © [2025] Rahul Majhi. All rights reserved.**

#### 1. Ownership and Rights
#This tool, "IP-Address-Class-Identifier," and all associated content, including but not limited to source code, designs, documentation, and functionality, are the intellectual property of Rahul Majhi. This tool is protected under copyright law and other intellectual property laws.

#### 2. Permitted Use
#You are granted a limited, non-exclusive, non-transferable license to use the tool for personal or commercial purposes, subject to the terms outlined herein.

#### 3. Restrictions
#Unless explicitly permitted in writing by the copyright holder:
#- You may not reproduce, distribute, or publicly display the tool, in whole or in part, without prior authorization.
#- You may not modify, reverse-engineer, or create derivative works based on the tool.
#- The tool must not be used for unlawful or malicious purposes.

#### 4. Attribution
#If the tool is used in any publication or project, appropriate credit must be given to the copyright holder as follows:
#*"IP-Address-Class-Identifier by Rahul Majhi. Copyright © [2025]. All rights reserved."*

#### 5. Disclaimer of Warranties
#This tool is provided "as is" without warranty of any kind. The copyright holder disclaims all warranties, either express or implied, including but not limited to the implied warranties of merchantability, fitness for a particular purpose, and non-infringement.

#### 6. Limitation of Liability
#In no event shall the copyright holder be liable for any damages arising out of the use or inability to use the tool, even if advised of the possibility of such damages.

#### 7. Governing Law
#This license shall be governed by and construed in accordance with the laws of Calcutta High Court.

#### 8. Termination
#This license is effective until terminated. Unauthorized use or violation of the terms will result in automatic termination of the license.

#For any inquiries or permissions beyond the scope of this license, please contact Rahul Majhi at [workforrdex@gmail.com].


#You can modify the placeholders, such as "[2025]" and "[Calcutta High Court]," based on your specifics. Let me know if you'd like further adjustments!
              ########




import ipaddress


def get_ip_class(ip):
    """Determine the class of the given IP address."""
    try:
        # Create an IPv4Address object
        ip_obj = ipaddress.IPv4Address(ip)

        # Determine the class based on the first octet
        first_octet = int(str(ip_obj).split('.')[0])

        if 0 <= first_octet <= 127:
            return "Class A"
        elif 128 <= first_octet <= 191:
            return "Class B"
        elif 192 <= first_octet <= 223:
            return "Class C"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "Class E (Reserved)"
        else:
            return "Invalid IP address"
    except ipaddress.AddressValueError:
        return "Invalid IP address"


if __name__ == "__main__":
    ip = input("Enter Targate IP address (e.g., 192.168.1.1): ")
    ip_class = get_ip_class(ip)
    print(f"The IP address {ip} belongs to: {ip_class}")