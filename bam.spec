Name:           bam
Version:        0.3.2
Release:        %mkrel 3
Summary:        A build-system
Group:          Development/Other
License:        MIT
URL:            http://matricks.github.com/bam/
Source0:        http://matricks.github.com/bam/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
%doc docs/bam.1.txt
%{_bindir}/%{name}
