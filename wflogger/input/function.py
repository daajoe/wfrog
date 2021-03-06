## Copyright 2009 Laurent Bovet <laurent.bovet@windmaster.ch>
##                Jordi Puigsegur <jordi.puigsegur@gmail.com>
##
##  This file is part of wfrog
##
##  wfrog is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import wfcommon.generic.wrapper

class FunctionInput(wfcommon.generic.wrapper.ElementWrapper):
    """
    Input receiving events as method calls. On any method call on this
    object, the first argument is considered being an event.
    Usually used as a registered !service.
    """

    send_event = None

    logger = logging.getLogger("input.function")

    def run(self, send_event):
        self.send_event = send_event

    def _call(self, attr, *args, **keywords):

        if self.send_event:
            self.logger.debug('Calling send_event')
            self.send_event(args[0])


