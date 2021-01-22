%global reponame crash-trace

Summary: Trace extension module for the crash utility
Name: crash-trace-command
Version: 3.0
Release: 0%{?dist}
License: GPLv2
Source: https://github.com/fujitsu/crash-trace/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-trace
ExclusiveOS: Linux
ExclusiveArch: x86_64 aarch64
BuildRequires: crash-devel >= 7.2.0-2
Requires: trace-cmd
Requires: crash >= 7.2.0-2

%description
Command for reading ftrace data from a dump file.

%prep
%autosetup -n %{reponame}-%{version}

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/crash/extensions/
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions/ %{_builddir}/%{reponame}-%{version}/trace.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/crash/extensions/trace.so
%doc COPYING

%changelog
* Fri Jan 22 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 3.0-0
- Initial crash-trace-command package
