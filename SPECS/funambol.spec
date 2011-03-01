Name:           funambol
Version:        9.0.0
Release:	    1%{?dist}
Summary:        funambol biserver	

Group:	        Network Servers
License:        GPL	
URL:		    https://www.forge.funambol.org/DomainHome.html
Source0:        funambol-9.0.0-x64.bin     	
Source1:        funambol
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Funambol Community Edition is free open source software that enables you to synchronize data between mobile devices and backend data sources, and to perform push email. It includes built-in functionality to perform mobile cloud sync. The software can also be used to build and deploy mobile data applications and services.

%prep
#%setup -c -T -a 0


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/
%{SOURCE0} 
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%defattr(0555,root,root,-)
/opt/Funambol
%{_sysconfdir}/init.d/funambol


%changelog
* Mon Feb 28 2010 Frederic Descamps <lefred@esquimaux.be> 9.0.0-1
- first rpm of funambol
