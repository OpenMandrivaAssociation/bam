Name:           bam
Version:        0.4.0
Release:        %mkrel 1
Summary:        A build-system
Group:          Development/Other
License:        MIT
URL:            http://matricks.github.com/bam/
Source0:        http://matricks.github.com/bam/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A tool that controls process of producing executables of 
software from its source code.

%prep
%setup -q

%build
sh -x make_unix.sh %{optflags}

%install
rm -rf %{buildroot}

install -D -m 0755 %{name} \
        %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc license.txt docs/*
%{_bindir}/%{name}
