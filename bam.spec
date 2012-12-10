Name:		bam
Version:	0.4.0
Release:	%mkrel 2
Summary:	A build-system
Group:		Development/Other
License:	MIT
URL:		http://matricks.github.com/bam/
Source0:	http://matricks.github.com/bam/%{name}-%{version}.tar.bz2

%description
A tool that controls process of producing executables of
software from its source code.

%prep
%setup -q

%build
sh -x make_unix.sh %{optflags}

%install
%__rm -rf %{buildroot}
%__install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc license.txt docs/*
%{_bindir}/%{name}


%changelog
* Mon Jan 30 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 769896
- Drop BuildRoot definition, minor spec cleanup

* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 0.4.0-1
+ Revision: 701975
- New version: 0.4.0

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-3mdv2011.0
+ Revision: 610037
- rebuild

* Mon Apr 26 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.3.2-2mdv2010.1
+ Revision: 539334
- fix %%description, remove useless line.

* Mon Apr 26 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 539311
- fix URL
- fix source0
- update to 0.3.2
- fix install

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.2.0-2mdv2010.0
+ Revision: 436768
- rebuild

* Tue Jan 20 2009 Olivier Thauvin <nanardon@mandriva.org> 0.2.0-1mdv2009.1
+ Revision: 332053
- mdv adapation from fedora spec

  + trem <trem@mandriva.org>
    - import bam


* Fri Jan 16 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.2.0-1
- Update to 0.2.0

* Sat Nov 01 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.0.0.4.3-1
- Honor optflags
- Select a 'better' code for version
- install in bindir
- Correct summary & description
- Remove needless documentation

* Sat Nov 01 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.0.0.for.teeworlds.0.4.3-1
- Initial Release
