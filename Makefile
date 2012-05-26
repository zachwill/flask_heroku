# A simple way to update Flask Heroku's static files.

# ----------------------
#  Useful variables
# ----------------------
NORM=\033[0m
BOLD=\033[1m
CHECK=\033[32m✔\033[39m
port=5000


# ----------------------
#  Default build
# ----------------------
build:
	@echo "\n⚡  ${BOLD}This might take a minute${NORM}  ⚡\n"
	@make clone
	@make update
	@make js
	@rm -rf {bootstrap,update}
	@echo "\n⚡  ${BOLD}Successfully updated${NORM}  ⚡\n"


# ----------------------
#  Clone Bootstrap && Make
# ----------------------
clone:
	@git clone git://github.com/twitter/bootstrap.git
	@echo "\n${BOLD}Clone Twitter Bootstrap...  ${NORM}${CHECK}\n"
	@cd bootstrap; make bootstrap
	@cd bootstrap; cp -R less bootstrap/css/less
	@cd bootstrap; mv bootstrap ../update


# ----------------------
#  External JavaScript
# ----------------------
js:
	@curl http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js > static/js/jquery.js
	@echo "\n${BOLD}Grab latest jQuery...  ${NORM}${CHECK}\n"
	@curl -L http://git.io/less-1.3.0 > static/js/less.js
	@echo "\n${BOLD}Grab latest LESS.js...  ${NORM}${CHECK}\n"
	@curl http://modernizr.com/downloads/modernizr-2.5.3.js > static/js/modernizr.js
	@echo "\n${BOLD}Grab latest Modernizr...  ${NORM}${CHECK}\n"


# ----------------------
#  Update commands
# ----------------------
update:
	@rm -rf static/css/less
	@mv update/css/* static/css
	@mv update/img/* static/img
	@mv update/js/* static/js
	@echo "\n${BOLD}Update static files...  ${NORM}${CHECK}\n"
