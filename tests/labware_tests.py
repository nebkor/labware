import unittest
import labware

class MicroplateTest(unittest.TestCase):

	expected_margin = 9 # ANSI standard.

	def a1_calibration_test(self):
		plate = labware.Microplate()
		plate.calibrate(x=10, y=10, z=10)
		self.assertEqual(plate.well('A1').coordinates(), (10, 10, 10))

	def a2_coordinate_test(self):
		plate = labware.Microplate()
		plate.calibrate(x=10, y=10, z=10)
		a2 = plate.well('A2').coordinates()
		self.assertEqual(a2, (10, 10+self.expected_margin, 10))

	def b1_coordinate_test(self):
		plate = labware.Microplate()
		plate.calibrate(x=10, y=10, z=10)
		b1 = plate.well('B1').coordinates()
		self.assertEqual(b1, (10+self.expected_margin, 10, 10))

	def b2_coordinate_test(self):
		plate  = labware.Microplate()
		plate.calibrate(x=10, y=10, z=10)
		b2 = plate.well('B2').coordinates()
		margin = self.expected_margin
		self.assertEqual(b2, (10+margin, 10+margin, 10))

	def coordinate_lowercase_test(self):
		plate  = labware.Microplate()
		plate.calibrate(x=10, y=10, z=10)
		b2 = plate.well('b2').coordinates()
		margin = self.expected_margin
		self.assertEqual(b2, (10+margin, 10+margin, 10))

	def deck_calibration_test(self):

		m_offset = 10

		config = {
			'calibration': {
				'a1': {
					'type':'microplate_96',
					'x': m_offset,
					'y': m_offset,
					'z': m_offset
				}
			}
		}

		deck = labware.Deck(a1=labware.Microplate())
		deck.configure(config)

		margin = self.expected_margin

		plate = deck.slot('a1')

		a1 = plate.well('a1').coordinates()
		b2 = plate.well('b2').coordinates()

		self.assertEqual(a1, (m_offset, m_offset, m_offset))
		self.assertEqual(b2, (m_offset+margin, m_offset+margin, m_offset))