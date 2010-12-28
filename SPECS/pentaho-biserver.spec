Name:           pentaho-biserver		
Version:        3.7.0	
Release:	2%{?dist}
Summary:        pentaho biserver	

Group:	        Network Servers
License:	GPL
URL:		http://community.pentaho.com
Source0:        biserver-ce-%{version}-stable.tar.gz	
Source1:        pentaho-biserver
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Pentaho BI server

%prep
%setup -c -T -a 0


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/
mv biserver-ce $RPM_BUILD_ROOT/opt/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/opt/biserver-ce
%defattr(0555,root,root,-)
%{_sysconfdir}/init.d/pentaho-biserver


%changelog
* Mon Dec 20 2010 Frederic Descamps <lefred@esquimaux.be> 3.7.0-1 
- first rpm of biserver
