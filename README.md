# libosip2 - rpm specs

## Build

```sh
git clone https://github.com/netxms/libosip2-rpm && cd libosip2-rpm

ARCH=$(arch)
REL=8
CONF=rocky+epel-$REL-$ARCH

mock -r $CONF --spec SPECS/libosip2.spec --sources SOURCES/libosip2-5.3.0.tar.gz
rsync -avz /var/lib/mock/$CONF/result/*.rpm $TARGET_USER@$TARGET_HOST:$TARGET_LOCATION/epel/$REL/$ARCH/stable/Packages/
```
