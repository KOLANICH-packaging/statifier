#!/usr/bin/env python3
"""Builds packages"""
import sys
from pathlib import Path
from prebuilder.systems import CMake, Make
from prebuilder.distros.debian import Debian
from prebuilder.buildPipeline import BuildPipeline, BuildRecipy
from prebuilder.repoPipeline import RepoPipelineMeta
from prebuilder.core.Package import PackageMetadata
from prebuilder.core.Package import PackageRef, VersionedPackageRef
from prebuilder.fetchers.GitRepoFetcher import GitRepoFetcher
from fsutilz import movetree, copytree
from ClassDictMeta import ClassDictMeta

thisDir = Path(".").absolute()




premakeMeta = {
	"descriptionShort": "cross-platform build script generator",
	"descriptionLong": "premake allows you to manage your project configuration in one place and still support those pesky IDE-addicted Windows coders and/or cranky Linux command-line junkies. It allows you to generate project files for tools that you do not own. It saves the time that would otherwise be spent manually keeping several different toolsets in sync. And it provides an easy upgrade path as new versions of your favorite tools are released.",
	"license": "BSD-3-Clause",
	"section": "devel",
}

class build(metaclass=RepoPipelineMeta):
	"""It's {maintainerName}'s repo for {repoKind} packages of build tools."""
	
	DISTROS = (Debian,)
	
	def statifier():
		repoURI = "https://github.com/KOLANICH/statifier"
		
		class cfg(metaclass=ClassDictMeta):
			descriptionShort = "Combine dynamic ELF executable libraries into one file"
			descriptionLong = """Puts a dynamically linked ELF executable and all its libraries (and
 all LD_PRELOAD libraries if any) into one file. This file can be
 copied and run on another machine without needing to drag along its
 libraries."""
			license = "GPL-2.0"
			section = "devel"
			homepage = repoURI
		
		bakeBuildRecipy = BuildRecipy(Make, GitRepoFetcher(repoURI, refspec="master"), buildOptions = {}, useKati=False)
		bakeMetadata = PackageMetadata("statifier", **cfg)
		
		return BuildPipeline(bakeBuildRecipy, ((Debian, bakeMetadata),))


if __name__ == "__main__":
	build()
