Name:           nss-mdns
Version:        0.10
Release:        0
Url:            http://0pointer.de/lennart/projects/nss-mdns/
Summary:        Host Name Resolution Via Multicast DNS (Zeroconf) for glibc
License:        LGPL-2.1+
Group:          Productivity/Networking/DNS/Utilities
Source:         %{name}-%{version}.tar.bz2
Source1:        nss-mdns-config
Source2:        baselibs.conf

%description
nss-mdns is a plug-in for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing a hostname
resolution via Multicast DNS (aka Zeroconf, aka Apple Rendezvous, aka
Apple Bonjour), and effectively allowing name resolution by common
Unix/Linux programs in the ad-hoc mDNS domain .local.

nss-mdns provides only client functionality, which means that you have
to run a mDNS responder daemon separately from nss-mdns if you want to
register the local hostname via mDNS. I recommend Avahi.

By default, nss-mdns tries to contact a running avahi-daemon to resolve
hostnames and addresses and makes use of its superior record cacheing.

%prep
%setup -q

%build
%configure --libdir=/%{_lib}

%install
%make_install
install -D -m0755 %{SOURCE1} %{buildroot}%{_sbindir}/nss-mdns-config

%post
/sbin/ldconfig
if [ "$1" -eq 1 ] ; then
    nss-mdns-config --enable
fi

%preun
if [ "$1" -eq 0 ] ; then
    nss-mdns-config --disable
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE
%{_sbindir}/nss-mdns-config
/%{_lib}/libnss_mdns.so.2
/%{_lib}/libnss_mdns_minimal.so.2
/%{_lib}/libnss_mdns4.so.2
/%{_lib}/libnss_mdns4_minimal.so.2
/%{_lib}/libnss_mdns6.so.2
/%{_lib}/libnss_mdns6_minimal.so.2
