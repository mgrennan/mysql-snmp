Name:           mysql-snmp
Version:        1.3rc3
Release:        1%{?dist}
Summary:        SNMP monitoring agent for MySQL

Group:          Applications/Databases
License:        GPL
URL:            http://www.masterzen.fr/software-contributions/mysql-snmp-monitor-mysql-with-snmp
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       perl(DBI), perl(DBD::mysql) >= 1.0, perl(Unix::Syslog)
Requires:       perl(SNMP), perl(NetSNMP::OID), perl(NetSNMP::agent), perl(NetSNMP::ASN)
Requires:       perl(NetSNMP::agent::default_store), perl(NetSNMP::default_store)
Requires:       perl(Math::BigInt::GMP)
Requires:       net-snmp >= 5.4.3
Obsoletes:      mysql-agent

%description
mysql-snmp is a small daemon that connects to a local snmpd daemon
to report statistics on a local or remote MySQL server.

%prep
%setup -q
test "$RPM_BUILD_ROOT" == "/" || rm -rf "$RPM_BUILD_ROOT"

%install
install -d ${RPM_BUILD_ROOT}%{_sbindir}
install -d ${RPM_BUILD_ROOT}%{_initrddir}
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install -d ${RPM_BUILD_ROOT}%{_datadir}/snmp/mibs
install -c -m 755 mysql-snmp ${RPM_BUILD_ROOT}%{_sbindir} 
install -c -m 755 redhat/mysql-snmp.init ${RPM_BUILD_ROOT}%{_initrddir}/%{name}
install -c -m 644 redhat/mysql-snmp.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
install -c -m 600 my.cnf ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp
install -c -m 644 mysql-snmp ${RPM_BUILD_ROOT}%{_mandir}/man1
gzip ${RPM_BUILD_ROOT}%{_mandir}/man1/mysql-snmp 
install -m 644 PERCONA-SERVER-MIB.txt ${RPM_BUILD_ROOT}%{_datadir}/snmp/mibs

%clean


%files
%defattr(-,root,root,-)
%doc COPYING README opennms/*
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/snmp/my.cnf
%doc %{_mandir}/man1/*
%{_initrddir}/*
%{_datadir}/snmp/mibs/*

%changelog
* Thu Apr 23 2015 Mark Grennan <mark@grennan.com> - 1.4rc3
- fixed variable type problems
* Wed Apr 15 2015 Mark Grennan <mark@grennan.com> - 1.3rc2
- Percona release v1.3rc2
* Tue Apr 14 2015 Mark Grennan <mark@grennan.com> - 1.3rc1
- Percona release v1.3rc1
* Thu Feb 17 2011 Brice Figureau <brice+debian@daysofwonder.com> - 1.2
- v1.2 release
* Wed Feb 17 2010 Robin Bowes <rpmbuild@yo61.net> - 1.0
- v1.0 release
* Mon Nov 16 2009 Robin Bowes <rpmbuild@yo61.net> - 1.0rc2-1
- Bump to rc2 version
* Sat Oct 31 2009 Brice Figureau <brice@daysofwonder.com> - 1.0rc1-1
- New version
* Sat Oct 24 2009 Brice Figureau <brice@daysofwonder.com> - 0.8-1
- New version
- Manpage compression in the spec
* Mon Sep 28 2009 Robin Bowes <rpmbuild@yo61.net> - 0.7-2
- Add opennms config files to package
* Mon Sep 28 2009 Robin Bowes <rpmbuild@yo61.net> - 0.7-1
- Initial RPM packaging
