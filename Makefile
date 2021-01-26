.PHONY: help
help:
	@echo
	@echo "Make Targets"
	@echo "============"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
	@echo

push_ll_notify:
	@echo "\n*************"
	@echo "components/ll_notify - Split and push"
	cd ../../.. ; \
		git subtree split --prefix homeassistant/components/ll_notify --annotate '(split) ' --rejoin --branch ll_notify_subtree2 ; \
		git push -f ll_notify_origin ll_notify_subtree2:master
clean:
	@echo "Reformat all code"

	@echo "\n*************"
	@echo "Reformat python"
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive  --exclude "js" .
	isort  --multi-line 2 --skip js .
	black  --exclude 'js/' .
	@echo "\n*************"
	@echo "Reformat JS"
	cd js ; npm run fix

build:
	@echo "\n*************"
	@echo "Build Frontend"
	cd js ; npm run build

screenshot.gif: tmp/screen_recording.mov
	ffmpeg -i tmp/screen_recording.mov -vf "fps=15,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse"  -loop 0 screenshot.gif
	ls -lh screenshot.gif

