%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	TransactHash
Summary:	Tie::TransactHash - Edit hash in transactions not changing order during trans.
Name:		perl-Tie-TransactHash
Version:	0.03
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Getopt-Mixed
BuildRequires:	perl-Tie-IxHash
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::TransactHash is a package which provides facilities for editing
any other hash in transactions.  A transaction is a group of changes
which go together and are either all applied or none.  When working on
a standard perl hash or a hash indexed DBM file, one advantage is that
the original hash remains untouched during the transaction, so its order
(the order the each(), keys() or values functions give out) is maintained
- changes can be made to the transact hash whilst iterating over it.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

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
