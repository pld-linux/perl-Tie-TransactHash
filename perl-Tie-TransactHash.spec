%include	/usr/lib/rpm/macros.perl
Summary:	Tie-TransactHash perl module
Summary(pl):	Modu³ perla Tie-TransactHash
Name:		perl-Tie-TransactHash
Version:	0.03
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-TransactHash-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Getopt-Mixed
BuildRequires:	perl-Tie-IxHash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-TransactHash perl module.

%description -l pl
Modu³ perla Tie-TransactHash.

%prep
%setup -q -n Tie-TransactHash-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/edit-db.pl
%{perl_sitelib}/Tie/TransactHash.pm
%{_mandir}/man[13]/*
