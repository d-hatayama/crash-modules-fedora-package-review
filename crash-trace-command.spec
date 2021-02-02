%global reponame crash-trace

Summary: Trace extension module for the crash utility
Name: crash-trace-command
Version: 3.0
Release: 1%{?dist}
License: GPLv2
Source: https://github.com/fujitsu/crash-trace/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-trace
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le s390x x86_64
BuildRequires: crash-devel >= 7.2.0-2
BuildRequires: gcc
Requires: trace-cmd
Requires: crash >= 7.2.0-2

%description
Command for reading ftrace data from a dump file.

%prep
%autosetup -n %{reponame}-%{version}

%build
%make_build

%install
install -m 0755 -d %{buildroot}%{_libdir}/crash/extensions/
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions/ %{_builddir}/%{reponame}-%{version}/trace.so

%clean
rm -rf %{buildroot}

%files
%{_libdir}/crash/extensions/trace.so
%license COPYING

%changelog
* Fri Jan 22 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 3.0-1
- Initial crash-trace-command package
