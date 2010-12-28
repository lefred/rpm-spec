Name:           impressive
Version:        0.10.3
Release:        1%{?dist}
Summary:        The stylish way of giving presentations

Group:          Applications/Productivity
License:        GPLv2
URL:            http://impressive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Impressive-%{version}.tar.gz
Source1:        %{name}.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
 
BuildArch:      noarch
Requires:       python-imaging
Requires:       pygame 
Requires:       PyOpenGL 
Requires:       opengl-games-utils
Requires:       xpdf
Requires:       xdg-utils
Requires:       opengl-games-utils

%if 0%{?fedora} > 10
Requires:       dejavu-sans-fonts
%endif

%if 0%{?fedora} <= 10
Requires:       dejavu-fonts
%endif

Provides:  keyjnote = %{version}-%{release}
Obsoletes: keyjnote < 0.10.2-3


%description
Impressive is a program that displays presentation slides. But unlike 
OpenOffice.org Impress or other similar applications, it does so with 
style. 

Smooth alpha-blended slide transitions are provided for the sake 
of eye candy, but in addition to this, Impressive offers some unique tools 
that are really useful for presentations.


%prep
%setup -q -n Impressive-%{version}


%build
# This package don't build anything, just copy files under build root.


%install
rm -rf $RPM_BUILD_ROOT
install -D -p -m 755 impressive.py $RPM_BUILD_ROOT%{_bindir}/python-impressive
install -D -p -m 644 impressive.1 $RPM_BUILD_ROOT%{_mandir}/man1/impressive.1
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc changelog.txt demo.pdf impressive.html license.txt
%{_bindir}/%{name}
%{_bindir}/python-%{name}
%{_mandir}/man1/*

%changelog
* Thu Oct 21 2010 Frederic Descamps <lefred@inuits.be> - 0.10.3-1
- Rebuilt for 0.10.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-6
- Added provides keyjnote.

* Mon Feb 16 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-5
- Obsolete keyjnote.

* Mon Feb 16 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-4
- Fix requires for dejavu fonts.

* Thu Feb 12 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-3
- Added OpenGL wrapper.
- Fix requires for dejavu fonts.

* Thu Feb 12 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-2
- Changed license.
- Added dejavu-fonts to requires.
- Added build section.

* Mon Feb  9 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-1
- Initial RPM release
