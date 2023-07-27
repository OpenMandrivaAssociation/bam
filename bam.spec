Name:		bam
Version:	0.5.1
Release:	1
Summary:	A build-system
Group:		Development/Other
License:	MIT
URL:		https://github.com/matricks/bam
Source0:	https://github.com/matricks/bam/archive/refs/tags/v%{version}.tar.gz

%description
A tool that controls process of producing executables of
software from its source code.

%prep
%autosetup -p1

%build
sh -x make_unix.sh %{optflags}

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc docs/*
%{_bindir}/%{name}
