%global tl_name gatherenum
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	A crossover of align* and enumerate
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gatherenum
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gatherenum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gatherenum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gatherenum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package (ab)uses the inline enumeration capabilities of enumitem to
add a "displayed" enumeration mode, triggered by adding 'gathered' to
the key-value option list of the enumerate environment. The end result
is similar to a regular enumerate environment wrapped in a multicols
environment, with the following advantages: Gathered enumerate can pack
items depending on their actual width rather than a fixed, constant
number per line. Gathered enumeration fills items in a line-major order
(instead of column-major order), which my students found less confusing.
YMMV. The package depends on enumitem, expl3, and xparse,

