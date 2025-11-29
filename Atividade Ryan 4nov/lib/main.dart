import 'package:flutter/material.dart';
import 'pages/perfil_card_page.dart';
import 'pages/login_page.dart';
import 'pages/chat_list_page.dart';
import 'pages/produtos_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const primaryPurple = Colors.deepPurple;

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Atividades Flutter',
      theme: ThemeData(
        
        colorScheme: ColorScheme.fromSeed(seedColor: primaryPurple),
        useMaterial3: true,
        
        
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            minimumSize: const Size(double.infinity, 50), 
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12), 
            ),
            elevation: 5, 
            
          ),
        ),
        
       
        appBarTheme: AppBarTheme(
          backgroundColor: primaryPurple.shade700,
          foregroundColor: Colors.white,
          centerTitle: true,
          elevation: 4, 
        ),
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  Widget _botaoMenu(BuildContext context, String titulo, Widget page) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 10),
      child: ElevatedButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => page),
          );
        },
        child: Text(
          titulo,
          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
   
    final colorScheme = Theme.of(context).colorScheme;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Atividades Flutter'),
      ),
      body: Container(
       
        decoration: BoxDecoration(
          gradient: LinearGradient(
            
            colors: [colorScheme.background, colorScheme.primaryContainer.withOpacity(0.3)],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.stretch, 
            children: [
              // Ícone para dar destaque
              Icon(
                Icons.palette_outlined,
                size: 80,
                color: colorScheme.primary,
              ),
              const SizedBox(height: 30),
              
              // Botões de navegação
              _botaoMenu(context, 'Atividade 1 - Card de Perfil', const PerfilCardPage()),
              _botaoMenu(context, 'Atividade 2 - Tela de Login', const LoginPage()),
              _botaoMenu(context, 'Atividade 3 - Lista de Chats', const ChatListPage()),
              _botaoMenu(context, 'Atividade 4 - Grid de Produtos', const ProdutosPage()),
              
              const SizedBox(height: 30),
              
              // Rodapé
              Text(
                'Navegue entre as atividades',
                textAlign: TextAlign.center,
                style: TextStyle(color: colorScheme.onBackground.withOpacity(0.6)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}