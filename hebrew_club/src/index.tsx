import 'react-native-gesture-handler';
import { createRoot } from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';

const rootElement = document.getElementById('root');
const root = createRoot(rootElement!);
root.render(<App />);

reportWebVitals();
