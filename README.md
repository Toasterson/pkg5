# OpenIndiana Image Packaging System

This is OpenIndiana's fork of the IPS package system, providing the `pkg(7)`
client, package publication tools, depot and zone integration. It rebases on
[omniosorg/pkg5](https://github.com/omniosorg/pkg5) and incorporates upstream work
from [oracle/solaris-ips](https://github.com/oracle/solaris-ips). See `README.sync`
for the imported upstream revisions.

Build on OpenIndiana with the system Python dependencies from
`developer/opensolaris/pkg5` installed. The default interpreter is Python 3.14;
set both `PYVER` and `PYVERSIONS` to select another supported version.

```sh
cd src
make all
make install
make packages BUILD_VERSION=5.11-0.151.1.8.1
make test JOBS=8
```

`make install` fills the workspace proto area; `make packages` publishes and
checks workspace packages. oi-userland supplies its release `BUILD_VERSION`.
The test target uses `pfexec` and writes per-interpreter results under `src/tests`.
Review those results: the make target allows individual test commands to fail.
Use `make fmt` for Black formatting and `make check` for Bandit and component
checks. Native compilation, service validation and tests require illumos.
