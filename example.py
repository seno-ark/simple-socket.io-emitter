# -*- coding: utf-8 -*-
#!/usr/bin/env python


from redis_emitter import Emitter

# create emitter instance
emitter = Emitter('localhost', 6379)

# event name
event = 'create_post'	

# payload
data = {'user': 'seno.ark', 'message': 'Hello, World!'}

# EMIT to default Namespace & default Room
emitter.emit(event, data)

# EMIT to Namespace / & default Room
emitter.nsp('/').emit(event, data)

# EMIT to Namespace / & Room episode_2
emitter.nsp('/').room('room_2').emit(event, data)
