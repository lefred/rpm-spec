Name:           funambol-ox-module
Version:        7.1.0
Release:	    1%{?dist}
Summary:        funambol ox module	

Group:	        Network Servers
License:        GPL	
URL:		    http://m2.funambol.org/repositories/artifacts/funambol/ox-module/7.1.0/
Source0:        ox-module-7.1.0.zip
Source1:        ox-listener
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       funambol


%description
Funambol's Open-Xchange (OX) synchronization 

%prep
%setup -c -T -a 0

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/Funambol/ds-server/modules/
cp Funambol/ox-connector/ox-connector-%{version}.s4j $RPM_BUILD_ROOT/opt/Funambol/ds-server/modules/
cd Funambol/ox-listener
unzip funambol-ox-listener-%{version}.zip
cp -r Funambol/* $RPM_BUILD_ROOT/opt/Funambol/
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%defattr(0555,root,root,-)
/opt/Funambol
%{_sysconfdir}/init.d/ox-listener



%changelog
* Mon Feb 28 2010 Frederic Descamps <lefred@esquimaux.be> 9.0.0-1
- first rpm of funambol ox module
