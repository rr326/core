# Test Configuration

This branch allows me to use a clean version of ha to test ll_notify (or any other customizations). It also allows me to keep the tests working.

I'm not sure I'll need it, but it seems a good way to track my past work where I had ll_notify included in core. (After this, ll_notify will be a custom component.)

## Tips

* Vscode in devcontainer. (and rebuild when upgrading)
* Test in virtualenv
```
cd tests/components/ll_notify
pytest .
```
