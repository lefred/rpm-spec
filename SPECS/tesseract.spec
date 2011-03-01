Name:		tesseract
Version:	3.00
Release:	1%{?dist}
Summary:	Raw OCR Engine 

Group:		Applications/File
License:	ASL 2.0
URL:		http://code.google.com/p/tesseract-ocr/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libtiff-devel

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.

%description devel
The %{name}-devel package contains header file for
developing applications that use %{name}.

%prep
%setup -q  

%build
sed -i 's#-DTESSDATA_PREFIX=@datadir@/#-DTESSDATA_PREFIX=@datadir@/%{name}/##' ccutil/Makefile.*
sed -i 's/#include <iostream>/#include <iostream>\n#include <cstdio>/' viewer/svutil.cpp
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/tesseract
mv $RPM_BUILD_ROOT%{_datadir}/tessdata $RPM_BUILD_ROOT%{_datadir}/tesseract
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/tessdata/{deu,fra,ita,nld,spa}*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/*training
%{_bindir}/unicharset_extractor
%{_bindir}/wordlist2dawg
%{_datadir}/%{name}

%doc AUTHORS ChangeLog COPYING eurotext.tif NEWS phototest.tif README 

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib%{name}*

%changelog
* Tue Dec 7 2010 Frederic Descamps <lefred at inuits.be> - 3.00-1
- Update to v3.00

* Wed Oct 21 2009 Karol Trzcionka <karlikt at gmail.com> - 2.04-1
- Update to v2.04
- Add static libraries to -devel subpackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 2.03-3
- include stdio.h for snprintf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May 04 2008 Karol Trzcionka <karlikt at gmail.com> - 2.03-1
- Update to v2.03
* Sat Feb 09 2008 Karol Trzcionka <karlikt at gmail.com> - 2.01-2
- Rebuild for gcc43
* Fri Sep 07 2007 Karol Trzcionka <karlikt at gmail.com> - 2.01-1
- Upgrade to v2.01
* Tue Aug 21 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-1
- Upgrade to v2.00
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.04-1
- Change url and source
- Update to v1.04
- Make patch bases on upstream's v1.04b
- Change compilefix patch
- Adding -devel subpackage
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-2
- Including patch bases on cvs
* Tue Feb 13 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-1
- Update to v1.03
* Sat Jan 26 2007 Karol Trzcionka <karlikt at gmail.com> - 1.02-3
- Update BRs
- Fix x86_64 compile
* Sat Dec 30 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-2
- Fixed rpmlint warning in SRPM
* Fri Dec 29 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-1
- Initial Release
