#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	TransactHash
Summary:	Tie::TransactHash - edit hash in transactions not changing order during trans
Summary(pl):	Tie::TransactHash - edycja hasza w transakcjach nie zmieniaj±cych kolejno¶ci
Name:		perl-Tie-TransactHash
Version:	0.03
Release:	11
# README claims "same as perl" and GPL v2+
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a25fc726b2f45cfaa6780b2cf3ccf0f
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Getopt-Mixed
BuildRequires:	perl-Tie-IxHash
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::TransactHash is a package which provides facilities for editing
any other hash in transactions.  A transaction is a group of changes
which go together and are either all applied or none.  When working on
a standard perl hash or a hash indexed DBM file, one advantage is that
the original hash remains untouched during the transaction, so its
order (the order the each(), keys() or values() functions give out) is
maintained - changes can be made to the transact hash whilst iterating
over it.

%description -l pl
Tie::TransactHash to pakiet udostêpniaj±cy mo¿liwo¶æ modyfikowania
innych haszy w transakcjach. Transakcja to grupa zmian, które albo s±
wykonywanie wszystkie, albo ¿adna. Przy pracy z normalnymi haszami
perlowymi lub plikiem DBM poindeksowanym haszem, zalet± jest to, ¿e
oryginalny hasz pozostaje nietkniêty podczas transakcji, wiêc jego
kolejno¶æ (kolejno¶æ, w jakiej zwracaj± warto¶ci funkcje each(),
keys() i values()) jest zachowana - zmainy mog± byæ robione w
transakcji podczas iteracji po haszu.

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
%doc README TODO
%attr(755,root,root) %{_bindir}/edit-db.pl
%{perl_vendorlib}/Tie/TransactHash.pm
%{_mandir}/man[13]/*
