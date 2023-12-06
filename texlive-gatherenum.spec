Name:		texlive-gatherenum
Version:	67201
Release:	1
Summary:	A crossover of align* and enumerate
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gatherenum
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gatherenum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gatherenum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gatherenum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package (ab)uses the inline enumeration capabilities of
enumitem to add a "displayed" enumeration mode, triggered by
adding 'gathered' to the key-value option list of the enumerate
environment. The end result is similar to a regular enumerate
environment wrapped in a multicols environment, with the
following advantages: Gathered enumerate can pack items
depending on their actual width rather than a fixed, constant
number per line. Gathered enumeration fills items in a
line-major order (instead of column-major order), which my
students found less confusing. YMMV. The package depends on
enumitem, expl3, and xparse,

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gatherenum
%{_texmfdistdir}/tex/latex/gatherenum
%doc %{_texmfdistdir}/doc/latex/gatherenum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
