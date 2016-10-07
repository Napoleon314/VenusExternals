import os, sys, multiprocessing, subprocess, glob
from build_util import *

def build_externals(bi):
	if not os.path.exists(build_cfg.external_path):
		os.makedirs(build_cfg.external_path)
	if os.path.isdir(build_cfg.external_path):
		additional_options = "-DCMAKE_INSTALL_PREFIX:STRING=\"INSTALL\""

		for fn in glob.glob(build_cfg.external_path + "/*"):
			if os.path.isdir(fn):
				sp = fn.split(build_cfg.external_path)[1][1:]
				print("Building %s..." % sp)
				build_path = build_cfg.build_path + "/" + build_cfg.external_path + "/" + sp
				script_path = "../../../../" + build_cfg.external_path + "/" + sp
				for info in bi.compilers:
					build_project(sp, build_path, bi, script_path, info, True, True, additional_options)

if __name__ == "__main__":
	cfg = cfg_from_argv(sys.argv)
	bi = build_info(cfg.compiler, cfg.archs, cfg.cfg)
	build_externals(bi)
 