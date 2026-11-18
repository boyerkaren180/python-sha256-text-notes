# Fingerprint UTF-8 content: implementation

## What the example does

SHA-256 fingerprints exact bytes. Different normalization or line endings produce different hashes; a plain hash does not authenticate the sender.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"hello"
```

Expected result:

```json
"2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
