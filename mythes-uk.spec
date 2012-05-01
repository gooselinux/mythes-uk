Name: mythes-uk
Summary: Ukrainian thesaurus
Version: 1.6.0
Release: 1.1%{?dist}
Source: http://downloads.sourceforge.net/ispell-uk/spell-uk-%{version}.tgz
Group: Applications/Text
URL: http://sourceforge.net/projects/ispell-uk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+
BuildRequires: perl
BuildArch: noarch

%description
Ukrainian thesaurus.

%prep
%setup -q -n spell-uk-%{version}

%build
cd src/thesaurus
mv -f th_uk_UA.dat th_uk_UA_v2.dat
../../bin/th_gen_idx.pl < th_uk_UA_v2.dat > th_uk_UA_v2.idx

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p src/thesaurus/th_uk_UA_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README README.uk COPYING.GPL COPYING.LGPL Copyright
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.6.0-1.1
- Rebuilt for RHEL 6

* Tue Aug 18 2009 Caolán McNamara <caolanm@redhat.com> - 1.6.0-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Caolán McNamara <caolanm@redhat.com> - 1.5.7-1
- initial version
