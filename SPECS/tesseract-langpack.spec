%define upstreamname tesseract
Name:		%{upstreamname}-langpack
Version:	2.00
Release:	6
Summary:	Langpacks for tesseract

Group:		Applications/File
License:	ASL 2.0
URL:		http://code.google.com/p/tesseract-ocr/
Source0:	http://tesseract-ocr.googlecode.com/files/%{upstreamname}-%{version}.deu.tar.gz
Source1:	http://tesseract-ocr.googlecode.com/files/%{upstreamname}-%{version}.fra.tar.gz
Source2:	http://tesseract-ocr.googlecode.com/files/%{upstreamname}-%{version}.ita.tar.gz
Source3:	http://tesseract-ocr.googlecode.com/files/%{upstreamname}-%{version}.nld.tar.gz
Source4:	http://tesseract-ocr.googlecode.com/files/%{upstreamname}-%{version}.spa.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%package de
Summary:	German langpack for %{upstreamname}
Group:		Applications/File
Requires:	%{upstreamname}

%package fr
Summary:	French langpack for %{upstreamname}
Group:		Applications/File
Requires:	%{upstreamname}

%package it
Summary:	Italian langpack for %{upstreamname}
Group:		Applications/File
Requires:	%{upstreamname}

%package nl
Summary:	Dutch langpack for %{upstreamname}
Group:		Applications/File
Requires:	%{upstreamname}

%package es
Summary:	Spanish langpack for %{upstreamname}
Group:		Applications/File
Requires:	%{upstreamname}

%description
%description de
German language data for %{upstreamname}.

%description fr
French language data for %{upstreamname}.

%description it
Italian language data for %{upstreamname}.

%description nl
Dutch language data for %{upstreamname}.

%description es
Spanish language data for %{upstreamname}.

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/tesseract
cp -a tessdata $RPM_BUILD_ROOT%{_datadir}/tesseract/
chmod -x $RPM_BUILD_ROOT%{_datadir}/tesseract/tessdata/*
rm -rf $RPM_BUILD_ROOT%{_datadir}/tesseract/eng*

%clean
rm -rf $RPM_BUILD_ROOT

%files fr
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/fra*

%files it
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/ita*

%files nl
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/nld*

%files es
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/spa*

%files de
%defattr(-,root,root,-)
%{_datadir}/%{upstreamname}/tessdata/deu*

%changelog
* Thu Dec 10 2009 Karol Trzcionka <karlikt at gmail.com> - 2.00-6
- Delete %%{?dist} macro

* Thu Dec 10 2009 Karol Trzcionka <karlikt at gmail.com> - 2.00-5
- Fix typo

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 24 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-2
- Fixed executable file in nl
* Tue Aug 21 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-1
- Initial Release
