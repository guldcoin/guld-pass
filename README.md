# guld-pass

__Very thin python3 client for [pass](https://passwordstore.org) (the standard unix password manager).__

This very small and simple script is a wrapper around `pass`. It is less secure, and slower than using pass directly. Use in cases where python is required.

### OfflineIMAP

This package was initially inspired by [OfflineIMAP](http://www.offlineimap.org/), and is a good compliment for it.

Example `.offlineimaprc`, assuming this source package is available at `/GPASS_DIR`:

```
[general]
pythonfile = /GPASS_DIR/guldpass/index.py

[Repository YourRemote]
remotepasseval = get_pass("Email/youraccount")
```

