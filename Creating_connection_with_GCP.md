To test your SSH key and ensure that you can connect to your Google Cloud Platform (GCP) Virtual Machine (VM), follow these steps:

---

### **1. Verify SSH Key Pair**

Ensure that you have both the private and public SSH key files:

- **Private Key**: Typically named `gcp_key` or similar.
- **Public Key**: Typically named `gcp_key.pub`.

If you haven't generated these keys, you can create them using:


```bash
ssh-keygen -t rsa -f ~/.ssh/gcp_key -C "your_username"
```


---

### **2. Add Public Key to GCP VM**

To allow SSH access, add your public key to your VM's metadata:

1. **Access VM Instances**:
   - Navigate to the [VM instances page](https://console.cloud.google.com/compute/instances) in the Google Cloud Console.

2. **Edit SSH Keys**:
   - Click on your VM instance.
   - Click the "Edit" button at the top.
   - Scroll down to the "SSH Keys" section.
   - Click "Add item" and paste the contents of your `gcp_key.pub` file.
   - Click "Save" to apply the changes.

---

### **3. Test SSH Connection**

Attempt to connect to your VM using the private key:


```bash
ssh -i ~/.ssh/gcp_key your_username@your_vm_external_ip
```


- **`your_username`**: The username associated with your SSH key.
- **`your_vm_external_ip`**: The external IP address of your VM.

If the connection is successful, you've correctly set up your SSH keys.

---

### **4. Troubleshooting**

If you encounter a "Permission denied (publickey)" error:

- **Ensure Correct Username**: The username should match the one associated with the SSH key added to the VM.
- **Verify Firewall Rules**: Ensure that your VM's firewall rules allow SSH traffic on port 22.
- **Check Key Permissions**: The private key file should have appropriate permissions:

  
```bash
  chmod 600 ~/.ssh/gcp_key
  ```


For a detailed guide on connecting to GCP VMs using SSH, refer to the [GCP documentation](https://cloud.google.com/compute/docs/connect/standard-ssh).

---

By following these steps, you can test and confirm that your SSH key is correctly configured for accessing your GCP VM. 
