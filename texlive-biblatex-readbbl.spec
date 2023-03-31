Name:		texlive-biblatex-readbbl
Version:	61549
Release:	2
Summary:	Read a .bbl file created by biber
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-readbbl
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-readbbl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-readbbl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package modifies the biblatex macro which reads a
.bbl file created by Biber. It is thus possible to include a
.bbl file into the main document with the filecontents
environment and send it to a publisher who does not need to run
the Biber program. However, when the bibliography changes one
has to create a new .bbl file.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-readbbl
%doc %{_texmfdistdir}/doc/latex/biblatex-readbbl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
