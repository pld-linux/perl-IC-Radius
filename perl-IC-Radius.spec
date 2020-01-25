#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	IC
%define		pnam	Radius
Summary:	IC::Radius - ICRADIUS interface module
Summary(pl.UTF-8):	IC::Radius - moduł interfejsu do ICRADIUS
Name:		perl-IC-Radius
Version:	0.4
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.innercite.com/pub/perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ecd7e2c89caac91c9167fd2c128b6d19
URL:		http://www.icradius.org/
BuildRequires:	perl-DBI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IC::Radius module provides functions for interfacing with
ICRADIUS.

%description -l pl.UTF-8
Moduł IC::Radius dostarcza funkcje do współpracy z ICRADIUS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/IC
%{perl_vendorlib}/IC/Radius.pm
%{_mandir}/man3/*
