Name:           bam
Version:        0.2.0

Release:        1%{?dist}
Summary:        A build-system

Group:          Amusements/Games
License:        Teeworlds and MIT
URL:            http://www.teeworlds.com
Source0:        http://www.teeworlds.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
A tool that controls process of producing executables of 
software from its source code. Used to build the Teeworlds game.


%prep
%setup -q 


%build
sh -x make_unix.sh %{optflags}


%install
rm -rf %{buildroot}

install -D -m 0755 src/%{name} \
        %{buildroot}%{_bindir}/%{name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc docs/bam.1.txt
%{_bindir}/%{name}


