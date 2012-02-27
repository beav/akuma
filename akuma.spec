%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: akuma
Summary: akuma daemonizer
Group: Internet/Applications
License: GPLv2
Version: 1.10
Release: 1%{?dist}
URL: http://java.net/projects/akuma
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: jna
Requires: java >= 0:1.6.0
#Requires: bouncycastle
%define __jar_repack %{nil}

%description
akuma

%prep
%setup -q

%build
ant -Dlibdir=/usr/share/akuma/lib/ clean package

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT/JAVAJAVAJAVA

%clean
rm -rf $RPM_BUILD_ROOT

%files
JAVAJAVAJAVA


%changelog
* Mon Feb 27 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Mon Feb 27 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Mon Feb 27 2012 Chris Duryee <cduryee@redhat.com> 1.8
- initial setup
