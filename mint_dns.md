### FIX MINT DNS 

* Install `unbound`:

```bash
sudo apt install unbound
```

* Disable `systemd-resolved`:

```bash
sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-resolved
```

* Config to use `unbound`:

Edit file `/etc/NetworkManager/NetworkManager.conf` and add after `plugins` in `[main]` region:
```bash
dns=unbound
```

* Enable `unbound` as service:

```bash
sudo systemctl enable unbound-resolvconf
sudo systemctl enable unbound
```

> source: https://sempreupdate.com.br/resolvendo-problemas-de-dns-no-ubuntu-17-04


Hard set DNS server to DHCP:

* Edit file `/etc/dhcp/dhclient.conf` and add:
```bash
supersede domain-name-servers 8.8.8.8, 8.8.4.4;
```

> source: https://unix.stackexchange.com/questions/136117/ignore-dns-from-dhcp-server-in-ubuntu


utils:
> https://wiki.archlinux.org/index.php/Openresolv
